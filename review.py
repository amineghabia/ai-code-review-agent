import sys
import io
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")


def main():
    if len(sys.argv) < 2:
        print("Usage: python review.py <file.py>")
        sys.exit(1)

    file_path = Path(sys.argv[1])
    if not file_path.exists():
        print(f"Error: file not found: {file_path}")
        sys.exit(1)

    code = file_path.read_text(encoding="utf-8")
    print(f"Reviewing {file_path}...\n", flush=True)

    from code_reviewer.agent import review_code
    report = review_code(code)

    print(report)

    output_path = Path(f"review_{file_path.stem}.md")
    output_path.write_text(report, encoding="utf-8")
    print(f"\n---\nReport saved → {output_path}", flush=True)


if __name__ == "__main__":
    main()
