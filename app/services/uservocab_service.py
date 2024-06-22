from app.models.uservocab import UserVocab
from app.mappers.uservocab_mapper import UserVocabMapper

class UserVocabService:
    def __init__(self):
        self.uservocab_mapper = UserVocabMapper()

    def select_page(self, page_num: int, page_size: int, course_filter: dict):
        return self.uservocab_mapper.select_all(course_filter).paginate(page_num, page_size, False).items

    def add(self, uservocab: UserVocab):
        self.uservocab_mapper.insert(uservocab)

    def update_by_id(self, uservocab: UserVocab):
        self.uservocab_mapper.update_by_id(uservocab)

    def delete_by_id(self, uservocab_id: int):
        self.uservocab_mapper.delete_by_id(uservocab_id)