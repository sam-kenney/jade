# Jade
Jade is a markdown renderer for Flask applications.

Initialise a new Jade project after installing with `python -m jade init`. This will create a simple Flask site with a home page, and a small blog, as an example of how to use the framework.

To get started, try editing the `content/home.md` file.

At the top of this file, you will see some `frontmatter`. This is `yaml` formatted content that is passed to the builder, and the template.

While not required, the following `frontmatter` is recommended for each of your pages.

* `permalink` - Where on the site you want the page to register. Defaults to the file's path within the `content` directory, without the file extension.
* `template` - the name of the template in your `templates` directory to render the content into. Defaults to `default`.

## Reserved names

* `page` - You can access the page frontmatter in your templates through the `page` variable. For example, the title for this page would be accessed with `page.title`.

* `pages` - The `pages` variable contains all subdirectories of the `content` directory. This can be useful for things such as rendering a blog home page, with a link to each post in a directory. Note that nested directories are not currently supported.

* `site` - You can also access site parameters, such as the site name through the `site` variable in all of your templates. Any parameters that you need globally should be added to the `.jade-config.yaml` file, under the site key. Try updating the `name` key under `site` in the config file.


## Contribution
Install development requirements with `pip install -r requirements-dev.txt`, then install `pre-commit` with `pre-commit install`. Ensure all `nox` tests are passing before creating a pull request.
