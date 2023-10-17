from flask import Blueprint, render_template, request, redirect,url_for,flash
from database import Session,Note
main_bp = Blueprint('main', __name__)

#################################################

@main_bp.route('/', methods=['POST'])
def index():
    task = request.form.get('task')  
    desc = request.form.get('desc')  

    if len(task) < 2:
        flash("too short input! title task less than 2 letters!", category='error')
    elif  len(desc) < 4:
        flash("too short input! Description less than 4 letters!", category='error')

    else:
        session = Session()

        try:
            new_note = Note(task=task, desc=desc)
            session.add(new_note)
            session.commit()
        except Exception as e:
            session.rollback()
            print(f"An error occurred: {e}")
           
    
        finally:
            session.close()
    return redirect(url_for("main.note_show"))




@main_bp.route('/', methods=['GET'])
def note_show():
    session = Session()

    try:        
        notes = session.query(Note).order_by(Note.id.desc()).all()
    except Exception as e:
        print(f"An error occurred while fetching notes: {e}")
        notes = []
    finally:
        session.close()
    return render_template("note.html", notes=notes)



@main_bp.route("/delete/<int:index>", methods=["POST"])
def delete(index):
    if index >= 0:
        session = Session()
        try:
            note_to_delete = session.query(Note).filter_by(id=index).first()
            if note_to_delete:
                session.delete(note_to_delete)
                session.commit()
            else:
                flash('Note not found', category='error')
        except Exception as e:
            print(f"An error occurred while deleting the note: {e}")
            session.rollback()
        finally:
            session.close()

    return redirect(url_for("main.index"))



@main_bp.route("/update/<int:index>", methods=["POST"])
def update(index):
    if index >= 0:
        session = Session()
        try:
            note_to_update = session.query(Note).filter_by(id=index).first()
            if note_to_update:
                new_task = request.form.get('new_task')
                new_desc = request.form.get('new_desc')
                if len(new_task) < 2:
                    flash("too short input! title task less than 2 letters!", category='error')
                elif  len(new_desc) < 4:
                    flash("too short input! Description less than 4 letters!", category='error')
                else:
                    note_to_update.task = new_task
                    note_to_update.desc = new_desc
                    session.commit()
            else:
                print("8888")
                flash('Note not found', category='error')
        except Exception as e:
            print(f"An error occurred while updating the note: {e}")
            session.rollback()
        finally:
            session.close()
    return redirect(url_for("main.index"))






