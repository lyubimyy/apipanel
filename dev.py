from flask import request
import json
from flask import Flask
from model import Domain, Event, Message, Version, db

app = Flask(__name__)


@app.route('/foo', methods=['POST'])
def foo():
    # if not request.json: abort(400)
    data = request.get_json(force=True)

    domain = Domain(
        domain=data['host']
    )
    db.session.add(domain)
    db.session.flush()
    event = Event(
        event=data['type'], domain_id = domain.id
    )
    db.session.add(event)

    version = Version(
        version=data['version'], domain_id = domain.id
    )
    db.session.add(version)

    message = Message(
        message=data['message'], domain_id = domain.id
    )
    db.session.add(message)

    db.session.commit()

    # domain_ev = db.session.query(Domain, Event).join(Event, Domain.id == Event.domain_id).all()
    # print(domain_ev)
    # domain_ev = db.session.query(Domain, Version).join(Version, Domain.id == Version.domain_id).all()
    # print(domain_ev)
    # domain_ev = db.session.query(Domain, Message).join(Message, Domain.id == Message.domain_id).all()
    # print(domain_ev)

    return json.dumps(request.json)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)




