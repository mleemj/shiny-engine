import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppComponent } from './app.component';
import {KnnModule} from './knn/knn.module';

@NgModule({
  declarations: [
    AppComponent
  ],
  imports: [
    BrowserModule,
    KnnModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
