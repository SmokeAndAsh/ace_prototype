def test_user_model(app):
    user = User()

    with app.app_context():
        db.session.add(user)
        db.session.commit()