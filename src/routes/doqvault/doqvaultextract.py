# @app.route('/', methods=['POST'])
# def main():
#     query_embedding = get_embeddings()
#     results = get_similarity_search(query_embedding)
#     response_data = [{"subject": result["metadata"]["subject"], "content": result["metadata"]["content"]} for result in results["matches"]]
#     return jsonify({"results": response_data})

# def get_similarity_search(query_embedding):
#     pc = Pinecone(
#         api_key="23fbd51e-82b6-41cf-b04a-e2891b3cbcab",
#         environment="us-east-1"
#     )

#     index = pc.Index("doq-vault")
   
#     response = index.query(
#         namespace="example-namespace",
#         vector=query_embedding,
#         top_k=3,  # Change top_k to 3 to get the top 3 results
#         include_metadata=True
#     )
#     return response

# def get_embeddings():
#     query = request.json['query']
#     query_embedding = openai_client.embeddings.create(
#         input=query,
#         model="text-embedding-3-small"
#     )
    
#     query_embedding = query_embedding.data[0].embedding
#     return query_embedding