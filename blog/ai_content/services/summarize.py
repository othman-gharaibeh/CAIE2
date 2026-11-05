# ai_content/services/summarize.py
from blog.models.post import Post
from .utils import validate_text_input, generate_ai_content



def _build_summarization_prompt(text):
    return f"Summarize the following blog post. The summary MUST be 500 characters or less:\n\n{text}"


def summarize_post(post_id):

    try:
        post_id_int = int(post_id)
        if post_id_int <= 0:
            raise ValueError("Post ID must be a positive integer.")
    except (ValueError, TypeError):
        raise ValueError("Invalid Post ID. It must be a positive integer.")


    try:
        post = Post.objects.get(pk=post_id_int)
    except Post.DoesNotExist:
        raise ValueError("Post not found.")


    raw_content = post.content if post.content else ""
    clean_content = validate_text_input(raw_content, min_length=10, field_name="Post content")


    prompt = _build_summarization_prompt(clean_content)


    summary = generate_ai_content(prompt)


    if len(summary) > 500:
        summary = summary[:500]

    return {
        "post_id": post.pk,
        "title": post.title,
        "summary": summary,
        "length": len(summary)
    }