import {NgModule} from '@angular/core';
import {RouterModule, Routes} from '@angular/router';
import {GreetingCompComponent} from './greeting-comp/greeting-comp.component';
import {GreetingGuard} from './greeting-guard';

const greetingRoutes: Routes = [
  {
    path: 'greeting',
    component: GreetingCompComponent,
    canActivate: [GreetingGuard]
  },
];

@NgModule({
  imports: [
    RouterModule.forChild(greetingRoutes)
  ],
  exports: [
    RouterModule
  ]
})
export class GreetingRoutingModule {
}
