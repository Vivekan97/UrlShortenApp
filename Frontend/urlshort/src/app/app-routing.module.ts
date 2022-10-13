import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { LoginComponent } from './login/login.component';
import { MainPageComponent } from './main-page/main-page.component';
import { RegisterComponent } from './register/register.component';

const routes: Routes = [
  {
    path:"home", component:MainPageComponent
  },
  {
    path:"signin", component:LoginComponent
  },
  {
    path:"register",component:RegisterComponent
  },
  {
    path:"**", redirectTo:"home",
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
