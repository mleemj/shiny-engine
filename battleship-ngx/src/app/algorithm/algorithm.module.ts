import {NgModule} from '@angular/core';
import {CommonModule} from '@angular/common';
import {AlgoMainComponent} from './algo-main/algo-main.component';
import {AlgoDetailComponent} from './algo-detail/algo-detail.component';
import {RouterModule} from '@angular/router';
import {AlgoDataBuilderComponent} from './algo-data-builder/algo-data-builder.component';
import {AlgoDataReaderComponent} from './algo-data-reader/algo-data-reader.component';
import {AlgoListComponent} from './algo-list/algo-list.component';
import {FormsModule} from '@angular/forms';
import {AlgoDataComponent} from './algo-data/algo-data.component';
import {AlgoRoutingModule} from './/algo-routing.module';
import { UploadDataComponent } from './upload-data/upload-data.component';
import { ViewDataComponent } from './view-data/view-data.component';

@NgModule({
  imports: [
    CommonModule,
    RouterModule,
    FormsModule,
    AlgoRoutingModule
  ],
  declarations: [
    AlgoMainComponent,
    AlgoDetailComponent,
    AlgoDataBuilderComponent,
    AlgoDataReaderComponent,
    AlgoListComponent,
    AlgoDataComponent,
    UploadDataComponent,
    ViewDataComponent],
  exports: [
    AlgoMainComponent,
    AlgoDetailComponent,
    AlgoDataBuilderComponent,
    AlgoDataReaderComponent,
    AlgoListComponent,
    AlgoDataComponent,
  UploadDataComponent,
  ViewDataComponent]
})
export class AlgorithmModule {
}
