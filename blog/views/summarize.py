from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..ai_content.services import summarize_post


@api_view(['POST'])
def summarize_post_view(request, post_id):
    try:

        result = summarize_post(post_id)
        return Response(result, status=status.HTTP_200_OK)

    except ValueError as e:
        error_msg = str(e)

        if error_msg == "Post not found.":
            return Response({"error": error_msg}, status=status.HTTP_404_NOT_FOUND)

        return Response({"error": error_msg}, status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        return Response(
            {"error": f"An unexpected error occurred: {str(e)}"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )