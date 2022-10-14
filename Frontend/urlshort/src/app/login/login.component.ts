import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormControl, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { LoginResponse } from '../_models/model';
import { AuthService } from '../_services/auth.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

  loginForm!:FormGroup;
  emailRegex:string = "^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,4}$";
  errorMessage!:string;

  constructor(private fb:FormBuilder, private auth:AuthService,
    private router:Router) { }

  ngOnInit(): void {
    if(this.auth.checkStatus()){
      this.router.navigate(["home"])
    }
    this.initializeForm();
  }

  initializeForm(){
    this.loginForm = this.fb.group({
      "email": new FormControl(null,[Validators.required, Validators.pattern(this.emailRegex)]),
      "password": new FormControl(null,[Validators.required, Validators.minLength(6)])
    })
  }

  loginUser(){
    // console.log("Login User");
    let username = this.loginForm.value["email"]
    let password = this.loginForm.value["password"]
    this.auth.loginUser(username, password).subscribe({
      next:(value:LoginResponse)=>{

        if(this.auth.setActiveUser(value)){
          this.router.navigate(["/home"])
        }
      },
      error:(err)=>{
        // console.log(err)
        this.errorMessage = err?.error?.message
      },
    })
  }

}
