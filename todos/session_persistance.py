class SessionPersistance:
    def __init__(self, session):
        self.session = session
        if 'lists' not in self.session:
            self.session['lists'] = []

    def all_lists(self):
        return self.session['lists']

    def find_list(self, list_id):
        found = (lst for lst in self.session['lists'] if lst['id'] == list_id)
        return next(found, None)
    
    def create_new_list(self, title):
        lists = self.all_lists()
        lists.append({
            'id': str(uuid4()),
            'title': title,
            'todos': [],
        })
        self.session.modified = True
    
    def update_list_by_id(self, list_id, new_title):
        lst = self.find_list(list_id)
        if lst:
            lst['title'] = new_title
            self.session.modified = True

    def delete_list(self, list_id):
        self.session['lists'] = [lst for lst in session['lists']
                        if lst['id'] != list_id]
        self.session.modified = True
        