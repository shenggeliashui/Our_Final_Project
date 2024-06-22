from app.models.vocab import Course
from app import db

class CourseMapper:
    @staticmethod
    def select_all(course_filter):
        return Course.query.filter(
            Course.name.like(f"%{course_filter['name']}%"),
            Course.no.like(f"%{course_filter['no']}%"),
            Course.teacher.like(f"%{course_filter['teacher']}%")
        ).order_by(Course.id.asc()).all()

    @staticmethod
    def insert(course):
        db.session.add(course)
        db.session.commit()

    @staticmethod
    def update_by_id(course):
        db.session.merge(course)
        db.session.commit()

    @staticmethod
    def delete_by_id(course_id):
        course = Course.query.get(course_id)
        if course:
            db.session.delete(course)
            db.session.commit()