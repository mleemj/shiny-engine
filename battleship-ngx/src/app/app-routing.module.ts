import {NgModule} from '@angular/core';
import {CommonModule} from '@angular/common';
import {RouterModule, Routes} from '@angular/router';
import {HomelandComponent} from './homeland/homeland/homeland.component';
import {AlgoMainComponent} from './algorithm/algo-main/algo-main.component';
import {AlgoListComponent} from './algorithm/algo-list/algo-list.component';
import {AlgoDetailComponent} from './algorithm/algo-detail/algo-detail.component';

const app_routes: Routes = [
  {path: '', redirectTo: '/home', pathMatch: 'full'},
  {path: 'home', component: HomelandComponent},
  {
    path: 'algo', component: AlgoMainComponent, children: [
    {path: 'algo_list', component: AlgoListComponent, outlet: 'port'},
    {path: 'algo_detail', component: AlgoDetailComponent, outlet: 'starboard'}
  ]
  }
];

@NgModule({
  imports: [
    CommonModule,
    RouterModule.forRoot(app_routes)
  ],
  exports: [RouterModule],
  declarations: []
})
export class AppRoutingModule {
}
