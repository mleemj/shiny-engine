import {NgModule} from '@angular/core';
import {BrowserModule} from '@angular/platform-browser';
import {FormsModule} from '@angular/forms';
import {CommonModule} from '@angular/common';
import {XSRFStrategy, CookieXSRFStrategy, Http} from '@angular/http';
import {HttpModule} from '@angular/http';

import {GreetingCompComponent} from './greeting-comp/greeting-comp.component';
import {GreetingFormComponent} from './greeting-form/greeting-form.component';
import {GreetingMsgComponent} from './greeting-msg/greeting-msg.component';
import {GreetingRoutingModule} from './greeting-routing.module';
import {GreetingGuard} from './greeting-guard';

import {CompIntrxnService} from './comp-intrxn.service';

@NgModule({
  imports: [
    BrowserModule,
    FormsModule,
    CommonModule,
    GreetingRoutingModule
  ],
  declarations: [
    GreetingCompComponent,
    GreetingFormComponent,
    GreetingMsgComponent
  ],
  providers: [CompIntrxnService, GreetingGuard, {
    provide: XSRFStrategy,
    useFactory: xsrfFactory
  }
  ]
})
export class GreetingModule {
}

export function xsrfFactory() {
  return new CookieXSRFStrategy('greeting-cookie', 'greeting-header');
}
