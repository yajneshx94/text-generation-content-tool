import wikipedia

def get_wikipedia_summary(topic):
    try:
        topic = topic.strip()
        print(f"Looking up topic: {topic}")

        search_results = wikipedia.search(topic)
        if not search_results:
            return "Sorry, I couldn't find that on Wikipedia."

        best_match = search_results[0]
        print(f"Best match found: {best_match}")

        # Fetch page object first
        page = wikipedia.page(best_match)
        summary = page.summary[:500]  # Limit summary length to avoid overflow

        print(f"\nWikipedia Summary:\n{summary}\n")
        return summary

    except wikipedia.exceptions.DisambiguationError as e:
        print(f"Disambiguation error: {e.options[:3]}")
        try:
            best_option = e.options[0]
            page = wikipedia.page(best_option)
            summary = page.summary[:500]
            return summary
        except Exception as inner_e:
            print(f"Failed to fetch disambiguation option: {inner_e}")
            return "Sorry, that topic has multiple meanings. Try being more specific."

    except wikipedia.exceptions.PageError:
        print("Page not found.")
        return "Sorry, I couldn't find that on Wikipedia."

    except Exception as e:
        print(f"Unexpected Error: {e}")
        return "Sorry, an unexpected error occurred while fetching Wikipedia data."
