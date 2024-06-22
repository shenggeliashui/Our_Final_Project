from app.models.vocab import Course
from app.mappers.vocab_mapper import CourseMapper

class CourseService:
    def __init__(self):
        self.course_mapper = CourseMapper()

    def select_page(self, page_num: int, page_size: int, course_filter: dict):
        return self.course_mapper.select_all(course_filter).paginate(page_num, page_size, False).items

    def add(self, course: Course):
        self.course_mapper.insert(course)

    def update_by_id(self, course: Course):
        self.course_mapper.update_by_id(course)

    def delete_by_id(self, course_id: int):
        self.course_mapper.delete_by_id(course_id)