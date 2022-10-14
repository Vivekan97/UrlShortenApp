import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Router } from '@angular/router';
import { BehaviorSubject, Observable, tap } from 'rxjs';
import { LoginResponse } from '../_models/model';
import { RootService } from './root.service';

@Injectable({
  providedIn: 'root'
})
export class AuthService {

  BaseUrl:string;

  isUserLoggedIn:BehaviorSubject<boolean> = new BehaviorSubject<boolean>(false)

  constructor(private http:HttpClient, private root:RootService, private router:Router) { 
    this.BaseUrl = this.root.getBaseUrl();
    this.checkStatus();
  }

  loginUser(username:string, password:string):Observable<LoginResponse>{
    let loginUrl:string = this.BaseUrl + "/auth/login";
    const loginForm:FormData = new FormData()
    loginForm.append("email",username)
    loginForm.append("password", password)
    const httpOptions = {
      headers: new HttpHeaders({
        "IgnoreAuth":"true"
      })
    }
    return this.http.post<LoginResponse>(loginUrl, loginForm, httpOptions)
  }

  registerUser(username:string, password:string):Observable<LoginResponse>{
    let registerUrl:string = this.BaseUrl + "/auth/register";
    const registerForm:FormData = new FormData()
    registerForm.append("email",username)
    registerForm.append("password", password)
    const httpOptions = {
      headers: new HttpHeaders({
        "IgnoreAuth":"true"
      })
    }
    return this.http.post<LoginResponse>(registerUrl, registerForm, httpOptions)
  }

  setActiveUser(user:LoginResponse):boolean{
    localStorage.setItem("accessToken",JSON.stringify(user.access_token))
    this.isUserLoggedIn.next(true);
    return true
  }

  getAccessToken():string | null{
    let token:string | null = localStorage?.getItem("accessToken")
    // console.log(token)
    if (!token || token===undefined || token===null || token==='undefined' || token==='null' || token===''){
      return null
    }
    return JSON.parse(token)
  }

  logOut(){
    this.isUserLoggedIn.next(false);
    localStorage.removeItem("accessToken");
    this.router.navigate(["/"])
  }

  get userStatus():Observable<boolean>{
    return this.isUserLoggedIn.asObservable();
  }

  checkStatus():boolean{
    if(this.getAccessToken()){
      this.isUserLoggedIn.next(true)
      return true
    }
    return false
  }
}
