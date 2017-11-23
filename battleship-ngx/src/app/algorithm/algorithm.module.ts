import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { AlgoMainComponent } from './algo-main/algo-main.component';
import { AlgoListComponent } from './algo-list/algo-list.component';
import { AlgoDetailComponent } from './algo-detail/algo-detail.component';
import {RouterModule} from '@angular/router';

@NgModule({
  imports: [
    CommonModule,
    RouterModule
  ],
  declarations: [AlgoMainComponent, AlgoListComponent, AlgoDetailComponent],
  exports: [AlgoMainComponent, AlgoListComponent, AlgoDetailComponent]
})
export class AlgorithmModule { }
