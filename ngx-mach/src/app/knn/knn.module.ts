import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { KnnComponent } from './knn.component';
import { KnnDataComponent } from './knn-data/knn-data.component';
import { FormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import { KnnFormComponent } from './knn-form/knn-form.component';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    HttpClientModule
  ],
  declarations: [KnnComponent, KnnDataComponent, KnnFormComponent],
  exports: [KnnComponent, KnnDataComponent, KnnFormComponent]
})
export class KnnModule { }
