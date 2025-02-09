import { Component, CUSTOM_ELEMENTS_SCHEMA } from '@angular/core';
import { DataService } from '../data.service';
import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';
import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'truncate'
})
export class TruncatePipe implements PipeTransform {
  transform(value: string, limit: number = 25, completeWords: boolean = false, ellipsis: string = '...'): string {
    if (!value) {
      return '';
    }

    if (value.length <= limit) {
      return value;
    }

    if (completeWords) {
      limit = value.substring(0, limit).lastIndexOf(' ');
    }

    return value.substring(0, limit) + ellipsis;
  }
}

@Component({
  selector: 'app-youtube-search',
  standalone: true,
  imports: [FormsModule, CommonModule, TruncatePipe],
  templateUrl: './youtube-search.component.html',
  styleUrls: ['./youtube-search.component.css'],
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class YoutubeSearchComponent {
  searchQuery: string = '';
  searchResults: any[] = [];
  message: string = '';

  constructor(private dataService: DataService) { }

  searchVideos(): void {
    this.dataService.searchYouTube(this.searchQuery).subscribe(
      (results) => {
        console.log(results);
        this.searchResults = results;
        this.message = '';
      },
      (error) => {
        console.error('Error searching videos:', error);
        this.message = 'Error searching videos.';
        this.searchResults = [];
      }
    );
  }

  saveVideo(video: any): void {
    this.dataService.saveVideo(video).subscribe(
      (response) => {
        this.message = 'Video saved!';
      },
      (error) => {
        console.error('Error saving video:', error);
        this.message = 'Error saving video.';
      }
    );
  }
}