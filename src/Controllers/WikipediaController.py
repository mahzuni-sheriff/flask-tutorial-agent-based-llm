from flask import request, jsonify
from services.Wikipedia import run_query  

def handle_query():
    query = request.args.get('q')
    if not query:
        return jsonify({"error": "Query parameter 'q' is required"}), 400
    
    try:
        answer = run_query(query)
        return jsonify({"answer": answer})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
