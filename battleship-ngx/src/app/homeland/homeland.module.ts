import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HomelandComponent } from './homeland/homeland.component';

@NgModule({
  imports: [
    CommonModule
  ],
  declarations: [HomelandComponent],
  exports: [HomelandComponent]
})
export class HomelandModule { }
