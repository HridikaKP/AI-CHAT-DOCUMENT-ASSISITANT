

from typing import List, Tuple, Dict

class ChatManager:
    """
    Handles RAG-style conversation: retrieves relevant documents,
    builds prompts, sends to LLM, and returns answers with sources.
    """
    def __init__(self, doc_handler, llm, config):
        self.doc_handler = doc_handler
        self.llm = llm
        self.config = config
        self.last_retrieved_sources: List = []

    def _build_system_instruction(self) -> str:
        return (
            "You are a helpful assistant. Use the provided documents to answer the user's question. "
            "If the documents do not contain the answer, say you don't know and provide best-effort reasoning."
        )

    def _assemble_prompt(
        self, query: str, history: List[Tuple[str, str]], retrieved: List
    ) -> List[Dict]:
        """
        Converts chat history and retrieved documents into messages for the LLM.
        """
        messages = [{"role": "system", "content": self._build_system_instruction()}]

        # Add last 10 messages from history
        for role, text in history[-10:]:
            role_name = "user" if role.lower() == "user" else "assistant"
            messages.append({"role": role_name, "content": text})

        # Build document context
        context_text = ""
        for doc in retrieved:
            meta = getattr(doc, "metadata", {})
            src = meta.get("source", "doc")
            snippet = getattr(doc, "page_content", "")[:1500]
            context_text += f"Source: {src}\n{snippet}\n---\n"

        # Final user message
        user_content = (
            f"Use the documents below to answer the question.\n\n"
            f"{context_text}\n"
            f"Question: {query}"
        )
        messages.append({"role": "user", "content": user_content})
        return messages

    def ask(self, query: str, history: List[Tuple[str, str]]) -> Tuple[str, List[Dict]]:
        # Retrieve top-K documents
        retrieved_docs = self.doc_handler.retrieve(query, top_k=self.config.TOP_K)
        self.last_retrieved_sources = retrieved_docs

        # Build LLM messages
        messages = self._assemble_prompt(query, history, retrieved_docs)

        # Call LLM
        ans_text, raw_response = self.llm.generate(
            messages=messages,
            max_tokens=512,
            temperature=0.0
        )

        # Debug if response is empty
        if not ans_text:
            print("LLM returned empty response. Raw API output:", raw_response)

        # Prepare sources for display
        sources = [
            {"source": getattr(doc.metadata, "get", lambda k, d=None: doc.metadata.get(k, d))("source", f"doc_{i}"),
             "score": getattr(doc, "score", None)}
            for i, doc in enumerate(retrieved_docs)
        ]

        return ans_text, sources
