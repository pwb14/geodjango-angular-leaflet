import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { HttpClient } from '@angular/common/http'

@Injectable({
  providedIn: 'root'
})
export class ShapeService {

  constructor(private http: HttpClient) { }

  getStateShapes(): Observable<any> {
    // this.http.get('http://localhost:8000/countries/country/').subscribe((data) => console.log(data))
    return this.http.get('http://localhost:8000/countries/country/')
  }

}
