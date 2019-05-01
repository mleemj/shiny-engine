# shiny-engine
<p>Welcome to <em>Matt's DIY Blog</em>, a very basic Django blogging website developed as an <a href="https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/django_assessment_blog">assessment task</a> for the Django learning module on the Mozilla Developer Network.</p>

<p>Working demo is hosted here <a href="https://matt-diy-blog.herokuapp.com/diy/">Matt DIY Blog<a/>

<h2>Features</h2>
The main features that have currently been implemented are:

<ul>
  <li>There are models for blog, blogger and blogcomments.</li>
  <li>User registration, login and logout.</li>
  <li>User can view list and detail information for blog and blogger.</li>
   <li>Blogger can make comments on blogs.</li>
  <li>Blogger can create and edit bio.</li>
  <li>Blogger can create, edit and delete blogs.</li>
</ul>

<h2>OAuth2 workflow</h2>
The main features that are currently implemented include:

<ul>
  <li>Blogger can register an OAuth2 client.</li>
  <li>Using client_credentials and passowrd grant-types, user can cURL request for an access token.</li>
  <li>Demo OAuth2 client is provided in this repository to demonstrate authorization code grant type.</li>
</ul>
