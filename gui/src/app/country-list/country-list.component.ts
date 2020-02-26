import { Component, OnInit } from '@angular/core';
import { Country } from '../country';
import { COUNTRIES } from '../mock-countries';


@Component({
  selector: 'app-country-list',
  templateUrl: './country-list.component.html',
  styleUrls: ['./country-list.component.scss']
})
export class CountryListComponent implements OnInit {
  countries = COUNTRIES;
  // country: Country = {
  //   id: 1,
  //   name: 'Botswana'
  // }

  constructor() { }

  ngOnInit() {
  }

}
