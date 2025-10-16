from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():  # put application's code here
    return render_template("index-3.html") #inside templates/

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/index.html')
def index():
    return render_template("index.html")

@app.route('/index-2.html')
def index2():
    return render_template("index-2.html")

@app.route('/index-3.html')
def index3():
    return render_template("index-3.html")

@app.route('/about-us.html')
def about():
    return render_template("about-us.html")

@app.route('/services.html')
def services():
    return render_template("services.html")

@app.route('/service-details.html')
def service_details():
    return render_template("service-details.html")

@app.route('/careers.html')
def careers():
    return render_template("careers.html")

@app.route('/career-single.html')
def career_single():
    return render_template("career-single.html")

@app.route('/team.html')
def team():
    return render_template("team.html")

@app.route('/testimonials.html')
def testimonials():
    return render_template("testimonials.html")

@app.route('/pricing-plan.html')
def pricing_plan():
    return render_template("pricing-plan.html")

@app.route('/faq.html')
def faq():
    return render_template("faq.html")

@app.route('/terms-conditions.html')
def terms_conditions():
    return render_template("terms-conditions.html")

@app.route('/privacy-policy.html')
def privacy_policy():
    return render_template("privacy-policy.html")

@app.route('/error-404.html')
def error_404():
    return render_template("error-404.html")

@app.route('/projects.html')
def projects():
    return render_template("projects.html")

@app.route('/project-single.html')
def project_single():
    return render_template("project-single.html")

@app.route('/shop-left-sidebar.html')
def shop_left_sidebar():
    return render_template("shop-left-sidebar.html")

@app.route('/shop-right-sidebar.html')
def shop_right_sidebar():
    return render_template("shop-right-sidebar.html")

@app.route('/shop-grid.html')
def shop_grid():
    return render_template("shop-grid.html")

@app.route('/product-single.html')
def product_single():
    return render_template("product-single.html")

@app.route('/cart.html')
def cart():
    return render_template("cart.html")

@app.route('/wishlist.html')
def wishlist():
    return render_template("wishlist.html")

@app.route('/checkout.html')
def checkout():
    return render_template("checkout.html")

@app.route('/login.html')
def login():
    return render_template("login.html")

@app.route('/register.html')
def register():
    return render_template("register.html")

@app.route('/blog-left-sidebar.html')
def blog_left_sidebar():
    return render_template("blog-left-sidebar.html")

@app.route('/blog-right-sidebar.html')
def blog_right_sidebar():
    return render_template("blog-right-sidebar.html")

@app.route('/blog-grid.html')
def blog_grid():
    return render_template("blog-grid.html")

@app.route('/blog-single-left-sidebar.html')
def blog_single_left_sidebar():
    return render_template("blog-single-left-sidebar.html")

@app.route('/blog-single-right-sidebar.html')
def blog_single_right_sidebar():
    return render_template("blog-single-right-sidebar.html")

@app.route('/blog-single-no-sidebar.html')
def blog_single_no_sidebar():
    return render_template("blog-single-no-sidebar.html")

@app.route('/posts-by-author.html')
def posts_by_author():
    return render_template("posts-by-author.html")

@app.route('/posts-by-date.html')
def posts_by_date():
    return render_template("posts-by-date.html")

@app.route('/posts-by-category.html')
def posts_by_category():
    return render_template("posts-by-category.html")

@app.route('/posts-by-tag.html')
def posts_by_tag():
    return render_template("posts-by-tag.html")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5016,debug=True)
