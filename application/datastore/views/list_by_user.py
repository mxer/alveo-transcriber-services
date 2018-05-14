from flask import abort, jsonify

from application.misc.event_router import EventRouter

class APIListByUser(EventRouter):
    def get(self, user_id):
        if user_id is None:
            abort(400, "User not specified")

        return self.event("datastore:list_by_user").handle(
                storage_key=key,
                user_id=user_id,
                revision=revision
            )