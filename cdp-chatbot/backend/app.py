from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# Load preprocessed data
with open('segment.json') as seg, open('mparticle.json') as mp, open('lytics.json') as ly, open('zeotap.json') as ze:
    segment_data = json.load(seg)
    mparticle_data = json.load(mp)
    lytics_data = json.load(ly)
    zeotap_data = json.load(ze)

def find_answer(question):
    if "segment" in question:
        return segment_data.get("setup_new_source", "Please check Segment documentation for setup details.")
    elif "mparticle" in question:
        return mparticle_data.get("create_user_profile", "Please check mParticle documentation for creating a profile.")
    elif "lytics" in question:
        return lytics_data.get("build_audience_segment", "Check Lytics documentation for audience segment creation.")
    elif "zeotap" in question:
        return zeotap_data.get("integrate_data", "See Zeotap documentation for data integration steps.")
    else:
        return "I support Segment, mParticle, Lytics, and Zeotap. Please ask about these platforms."

@app.route('/query', methods=['POST'])
def query():
    question = request.json.get('question', '').lower()
    answer = find_answer(question)
    return jsonify({"answer": answer})

if __name__ == '__main__':
    app.run(debug=True)
