import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule, Routes} from '@angular/router';
import {AlgoDataComponent} from './algo-data/algo-data.component';
import {AlgoDataBuilderComponent} from './algo-data-builder/algo-data-builder.component';
import {AlgoDataReaderComponent} from './algo-data-reader/algo-data-reader.component';
import {ViewDataComponent} from './view-data/view-data.component';
import {UploadDataComponent} from './upload-data/upload-data.component';

const algo_routes: Routes = [
  {path: 'game', component: AlgoDataComponent, children: [
    {path: 'build', component: AlgoDataBuilderComponent},
    {path: 'read', component: AlgoDataReaderComponent, children: [
      {path: '', component: ViewDataComponent, outlet: 'dorsal'},
      {path: '', component: UploadDataComponent, outlet: 'ante'}
    ]}
  ]}
];
@NgModule({
  imports: [
    CommonModule,
    RouterModule.forChild(algo_routes)
  ],
  exports: [
    RouterModule
  ],
  declarations: []
})
export class AlgoRoutingModule { }
