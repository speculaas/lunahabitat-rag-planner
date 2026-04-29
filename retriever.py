from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re


TOKEN_RE = re.compile(r"[a-z0-9]+")
STOPWORDS = {
    "a",
    "an",
    "and",
    "any",
    "at",
    "be",
    "before",
    "but",
    "by",
    "for",
    "if",
    "in",
    "is",
    "it",
    "its",
    "no",
    "non",
    "not",
    "of",
    "on",
    "or",
    "so",
    "that",
    "the",
    "their",
    "this",
    "to",
    "treat",
    "up",
    "used",
    "until",
    "with",
}


def _tokenize(text: str) -> set[str]:
    return {
        token
        for token in TOKEN_RE.findall(text.lower())
        if token not in STOPWORDS
    }


def _title_from_filename(path: Path) -> str:
    return path.stem.replace("-", " ").title()


@dataclass
class GuidanceChunk:
    """A retrieved chunk of local guidance text."""

    doc_id: str
    title: str
    content: str
    score: int


class CorpusRetriever:
    """Tiny keyword-based retriever for the local markdown corpus."""

    def __init__(self, docs_path: str | Path):
        self.docs_path = Path(docs_path)
        self._chunks = self._load_chunks()

    def _load_chunks(self) -> list[tuple[str, str, str, set[str]]]:
        chunks: list[tuple[str, str, str, set[str]]] = []
        for path in sorted(self.docs_path.glob("*.md")):
            if path.name == "README.md":
                continue
            text = path.read_text(encoding="utf-8")
            parts = [
                part.strip()
                for part in re.split(r"\n\s*\n", text)
                if part.strip()
            ]
            title = _title_from_filename(path)
            for part in parts:
                tokens = _tokenize(f"{title} {part}")
                if tokens:
                    chunks.append((path.name, title, part, tokens))
        return chunks

    def retrieve(self, query: str, top_k: int = 2) -> list[GuidanceChunk]:
        """Return the most relevant chunks for the given query."""
        query_tokens = _tokenize(query)
        if not query_tokens:
            return []

        ranked: list[GuidanceChunk] = []
        for doc_id, title, content, chunk_tokens in self._chunks:
            score = len(query_tokens & chunk_tokens)
            if score > 0:
                ranked.append(
                    GuidanceChunk(
                        doc_id=doc_id,
                        title=title,
                        content=content,
                        score=score,
                    )
                )

        ranked.sort(key=lambda chunk: (-chunk.score, chunk.title, chunk.content))
        return ranked[:top_k]
