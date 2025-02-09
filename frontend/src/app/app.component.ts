import { Component, OnInit } from '@angular/core';
import { DataService } from './data.service';
import { RouterModule } from '@angular/router';  // Import RouterModule
import { CommonModule } from '@angular/common';
import { YoutubeSearchComponent } from './youtube-search/youtube-search.component'; // Import YoutubeSearchComponent
import { HomeComponent } from './home/home.component'; // Import HomeComponent

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule, RouterModule, YoutubeSearchComponent, HomeComponent],  // Add RouterModule to imports, Import YoutubeSearchComponent,
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
  title(title: any) {
    throw new Error('Method not implemented.');
  }
  data: any;  // Declare the 'data' property
  message: string = '';

  constructor(private dataService: DataService) { }

  ngOnInit(): void {
    this.dataService.getData().subscribe(
      (response) => {
        this.data = response;
        console.log('Data from backend:', this.data);
      },
      (error) => {
        console.error('Error fetching data:', error);
      }
    );
  }

  submitData(event: Event): void{ // Declare the 'submitData' method
    event.preventDefault();
    this.dataService.postData({key:'value'}).subscribe(
      (response) => {
        console.log(response)
        this.message = 'Data sent to backend!';
      },
      (error) => {
        console.log(error)
        this.message = 'Error sending data!';
      }
    );
  }
}
