import wikipedia

def get_wikipedia_summary(topic):
    topic = topic.strip()
    print(f"Looking up topic: {topic}")

    try:
        search_results = wikipedia.search(topic)
        if not search_results:
            print("No results found.")
            return "Sorry, I couldn't find that on Wikipedia."

        # Try exact match, else pick best guess
        best_match = next((title for title in search_results if title.lower() == topic.lower()), search_results[0])
        print(f"Best match found: {best_match}")

        try:
            page = wikipedia.page(best_match)
            summary = page.summary[:500]  # Truncate to avoid overflow
            print("Wikipedia summary fetched successfully.")
            return summary

        except wikipedia.exceptions.DisambiguationError as e:
            print(f"Disambiguation error, options: {e.options[:3]}")
            try:
                disambiguated_page = wikipedia.page(e.options[0])
                summary = disambiguated_page.summary[:500]
                return summary
            except Exception as inner_e:
                print(f"Failed disambiguation fetch: {inner_e}")
                return "Sorry, that topic has multiple meanings. Try being more specific."

    except wikipedia.exceptions.PageError:
        print("Page not found.")
        return "Sorry, I couldn't find that on Wikipedia."

    except Exception as e:
        print(f"Unexpected Error: {e}")
        return "Sorry, an unexpected error occurred while fetching Wikipedia data."
