import {NgModule} from '@angular/core';
import {CommonModule} from '@angular/common';
import {RouterModule, Routes} from '@angular/router';
import {HomelandComponent} from './homeland/homeland/homeland.component';
import {AlgoMainComponent} from './algorithm/algo-main/algo-main.component';
import {AlgoDetailComponent} from './algorithm/algo-detail/algo-detail.component';
import {AlgoDataBuilderComponent} from './algorithm/algo-data-builder/algo-data-builder.component';
import {AlgoDataReaderComponent} from './algorithm/algo-data-reader/algo-data-reader.component';
import {AlgoListComponent} from './algorithm/algo-list/algo-list.component';

const app_routes: Routes = [
  {path: '', redirectTo: '/home', pathMatch: 'full'},
  {path: 'home', component: HomelandComponent},
  {
    path: 'algo', component: AlgoMainComponent, children: [
    {path: 'algo_list', component: AlgoListComponent, outlet: 'port'},
    {path: 'algo_detail', component: AlgoDetailComponent, outlet: 'starboard'}
  ]
  },
  {
    path: 'data', component: AlgoMainComponent, children: [
    {path: 'build_data', component: AlgoDataBuilderComponent, outlet: 'port'},
    {path: 'read_data', component: AlgoDataReaderComponent, outlet: 'starboard'}
  ]
  }
];

@NgModule({
  imports: [
    CommonModule,
    RouterModule.forRoot(app_routes, {enableTracing: true})
  ],
  exports: [RouterModule],
  declarations: []
})
export class AppRoutingModule {
}
