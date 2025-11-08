import openai
import os

# Use environment variable for OpenAI API key (set via terminal: export OPENAI_API_KEY=your_key)
openai.api_key = os.environ.get('OPENAI_API_KEY', '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')  # Replace with your key or set env var

def ai_tagline():
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": "Generate a catchy tagline for Mastersolis Infotech, an AI-powered company."}]
    )
    return response['choices'][0]['message']['content'].strip()

def ai_summarize(text):
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": f"Summarize this text concisely: {text}"}]
    )
    return response['choices'][0]['message']['content'].strip()

def ai_parse_resume(resume_text):
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": f"Extract skills, experience, and education from this resume: {resume_text}"}]
    )
    return response['choices'][0]['message']['content'].strip()

def ai_job_fit(resume_text, job_desc):
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": f"Compare this resume to the job description and give a fit score (0-100%) and notes: Resume: {resume_text} Job: {job_desc}"}]
    )
    content = response['choices'][0]['message']['content'].strip()
    # Parse score and notes (simple split)
    lines = content.split('\n')
    score = int(lines[0].split('%')[0]) if '%' in lines[0] else 50
    notes = '\n'.join(lines[1:])
    return score, notes

def ai_chatbot(question):
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": f"Answer as a company chatbot for Mastersolis Infotech: {question}"}]
    )
    return response['choices'][0]['message']['content'].strip()

def ai_build_resume(data):
    prompt = f"Generate a professional resume text from: Education: {data['education']}, Skills: {data['skills']}, Experience: {data['experience']}"
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content'].strip()

def ai_admin_digest():
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": "Summarize recent activity for Mastersolis admin dashboard."}]
    )
    return response['choices'][0]['message']['content'].strip()