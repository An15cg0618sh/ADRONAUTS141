from models import Session, Resume, Contact

def save_resume(name, email, resume_text, score, notes):
    session = Session()
    resume = Resume(name=name, email=email, resume_text=resume_text, score=score, notes=notes)
    session.add(resume)
    session.commit()
    session.close()

def save_contact(name, email, message):
    session = Session()
    contact = Contact(name=name, email=email, message=message)
    session.add(contact)
    session.commit()
    session.close()

def get_resume_count():
    session = Session()
    count = session.query(Resume).count()
    session.close()
    return count

def get_contact_count():
    session = Session()
    count = session.query(Contact).count()
    session.close()
    return count