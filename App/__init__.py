from flask            import Flask, request, render_template, flash, redirect, url_for
from App.config       import config
from App.Model        import db, Store
from datetime 		  import datetime
from sqlalchemy 	  import func

from shortuuid        import ShortUUID
from time             import time
from secrets          import token_hex

from App.form         import Form

from flask_wtf.csrf import CSRFProtect

def create_app(config_name):

    app = Flask(__name__)
    app.config.from_object(config[config_name])

    csrf = CSRFProtect()
    csrf.init_app(app)

    db.init_app(app)

    
    with app.app_context():
        db.create_all()
    
    config[config_name].init_app(app)
    
    @app.route('/', methods=['GET'])
    def init():
        store = Store.query.all()
        total = 0
        if store:
            values = [item.price for item in store]
            for val in values:
                total += val
        return render_template('content/index.htm', store=store, total=total)


    @app.route('/add-item', methods=['GET'])
    def add_item():
        form  = Form()
        # flash('hello world', 'danger')
        return render_template('content/add-item.htm', form=form)

    @app.route('/add-item', methods=['POST'])
    def add_itemp():
        form = Form(request.form)
        if form.validate_on_submit():
            flash('Item Added to inventory successfully!', 'success')
            return redirect(url_for('init'))

        else:
            print(form.errors)
            return render_template('content/add-item.htm', form=form)

    @app.route('/delete-item/<pk>', methods=['GET'])
    def delete_item(pk):
        item = Store.query.filter_by(public_key=pk).first()
        item.delete()
        item.commit()
        flash('Item Deleted successfully', 'info')
        return redirect(url_for('init'))


    return app


