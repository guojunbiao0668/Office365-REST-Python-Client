from office365.sharepoint.base_entity import BaseEntity


class PointPublishingSiteStatus(BaseEntity):

    @property
    def entity_type_name(self):
        return "SP.Publishing.PointPublishingSiteStatus"
