def analyze_document(text: str) -> dict:
    return {
        "summary": "Prototype summary output",
        "key_points": ["Point 1", "Point 2"],
        "questions": ["What is the main idea?"]
    }


if __name__ == "__main__":
    sample_text = "This is a sample document."
    result = analyze_document(sample_text)
    print(result)
