class FileSaver:
    def save_html(self, content, filename="references.html"):
        """Save the generated HTML to a file."""
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)
