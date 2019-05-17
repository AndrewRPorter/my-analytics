from dataclasses import dataclass


@dataclass
class MOZ_PLACE:
    id: int
    url: str
    title: str
    rev_host: str
    visit_count: int
    hidden: int
    typed: int
    frecency: str
    last_visit_date: float
    guid: str
    foreign_count: int
    url_hash: int
    description: str
    preview_image_url: str
    origin_id: int

    def __str__(self):
        return str(self.url)


@dataclass
class MOZ_HISTORYVISIT:
    id: int
    from_visit: int
    place_id: int
    visit_date: int
    visit_type: int
    session: int

    def __str__(self):
        return str(self.id)
