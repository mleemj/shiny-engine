import {BrowserModule} from '@angular/platform-browser';
import {NgModule} from '@angular/core';
import {FormsModule} from '@angular/forms';
import {HttpModule} from '@angular/http';

import {AppComponent} from './app.component';
import {AppRoutingModule} from './app-routing.module';
import {GreetingModule} from './greeting/greeting.module';
import {LandingComponent} from './landing/landing.component';

@NgModule({
  imports: [
    BrowserModule,
    FormsModule,
    HttpModule,
    GreetingModule,
    AppRoutingModule,
  ],
  declarations: [
    AppComponent,
    LandingComponent
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule {
}
