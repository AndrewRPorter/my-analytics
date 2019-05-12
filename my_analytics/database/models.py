from typing import Dict


class MOZ_PLACE:
    def __init__(self, data: Dict):
        __tablename__ = "moz_places"

        self.data = data
        self.id = data["id"]
        self.url = data["url"]
        self.title = data["title"]
        self.rev_host = data["rev_host"]
        self.visit_count = data["visit_count"]
        self.hidden = data["hidden"]
        self.typed = data["typed"]
        self.frecency = data["frecency"]
        self.last_visit_date = data["last_visit_date"]
        self.guid = data["guid"]
        self.foreign_count = data["foreign_count"]
        self.url_hash = data["url_hash"]
        self.description = data["description"]
        self.preview_image_url = data["preview_image_url"]
        self.origin_id = data["origin_id"]

    def to_dict(self):
        """
        Returns model data in dictionary format
        """
        return self.data

    def __repr__(self):
        return (f"<MOZ_PLACE(id='{self.id}', url='{self.url}', title='{self.title}', "
                f"rev_host='{self.rev_host}', visit_count='{self.visit_count}', "
                f"hidden='{self.hidden}', typed='{self.typed}', frecency='{self.frecency}', "
                f"last_visit_date='{self.last_visit_date}', guid='{self.guid}', "
                f"foreign_count='{self.foreign_count}', url_hash='{self.url_hash}', "
                f"description='{self.description}', preview_image_url='{self.preview_image_url}', "
                f"origin_id='{self.origin_id}')>")
    
    def __str__(self):
        return str(self.url)

class MOZ_HISTORYVISIT:
    def __init__(self, data: Dict):
        __tablename__ = "moz_historyvisits"

        self.data = data
        self.id = data["id"]
        self.from_visit = data["from_visit"]
        self.place_id = data["place_id"]
        self.visit_date = data["visit_date"]
        self.visit_type = data["visit_type"]
        self.session = data["session"]

    def to_dict(self):
        """
        Returns model data in dictionary format
        """
        return self.data

    def __repr__(self):
        return (f"<MOZ_HISTORYVISIT(id='{self.id}', from_visit='{self.from_visit}', "
                f"place_id='{self.place_id}', visit_date='{self.visit_date}', "
                f"visit_type='{self.visit_type}', session='{self.session}')>")
    
    def __str__(self):
        return str(self.id)