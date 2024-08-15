from flask import request, jsonify
from services.Wikipedia.Wikipedia import runQuery 

def handle_query():
    query = request.args.get('q')
    if not query:
        return jsonify({"error": "Query parameter 'q' is required"}), 400
    
    try:
        answer = runQuery(query)
        return jsonify({"answer": answer})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
