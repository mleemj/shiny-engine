**ng-cli**

`Install nodejs and npm`

`npm install -g @angular/cli`

`ng new project <<project_name>>`

**Install Bootstrap and JQuery**

`npm install --save bootstrap`

`npm install --save jquery`

_Add bootstrap style and jquery js to angular-cli.json_

`"styles": [
    "styles.css",
    "../node_modules/bootstrap/dist/css/bootstrap.min.css"
  ],
  "scripts": [
    "../node_modules/jquery/dist/jquery.min.js",
    "../node_modules/bootstrap/dist/js/bootstrap.min.js"
  ],`

**Install ng-boostrap**

`npm install --save @ng-bootstrap/ng-bootstrap`

_Add NgbModule.forRoot() to app.module_

  `imports: [NgbModule.forRoot(), ...],`

_Add NgbModule to app children modules._

  `imports: [NgbModule, ...]`
  
**Id vs Name**

`Css used Id. Like Label for='<<id>>'`

`Name of the element. For example used by the server to identify the fields in form submits.
`

