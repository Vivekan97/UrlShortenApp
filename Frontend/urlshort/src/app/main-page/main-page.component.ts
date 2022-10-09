import { Component, OnInit } from '@angular/core';
import { ShortUrlResponse } from '../_models/model';
import { UrlShortService } from '../_services/url-short.service';

@Component({
  selector: 'app-main-page',
  templateUrl: './main-page.component.html',
  styleUrls: ['./main-page.component.css']
})
export class MainPageComponent implements OnInit {

  inputUrl!:string;
  isLoading:boolean = false;
  isError:boolean = false;
  errorMessage!:string;
  resultUrl!:string;

  constructor(private url:UrlShortService) { }

  ngOnInit(): void {
  }

  fetchShortUrl(){
    
    this.cleanPage();
    // console.warn(this.inputUrl);
    this.url.getShortenedUrl(this.inputUrl).subscribe(
      {
        next:(value:ShortUrlResponse)=>{
            // console.log(value)
            this.resultUrl = value.result;
        },
        error:(err:any)=>{
            this.isError = true;
            this.isLoading = false;
            this.errorMessage = err?.error?.message
            console.log(err)
        },
        complete:()=>{
            this.isLoading = false
        },
      }
    )
  }

  fetchLongUrl(){
    
    this.cleanPage();
    // console.warn(this.inputUrl);
    this.url.getLongUrl(this.inputUrl).subscribe(
      {
        next:(value:ShortUrlResponse)=>{
            // console.log(value)
            this.resultUrl = value.result;
        },
        error:(err:any)=>{
            this.isError = true;
            this.isLoading = false;
            this.errorMessage = err?.error?.message
            console.log(err)
        },
        complete:()=>{
            this.isLoading = false
        },
      }
    )
  }


  cleanPage(){
    this.isLoading = true;
    this.isError = false;
    this.resultUrl = "";
    this.errorMessage = "";
  }

}
