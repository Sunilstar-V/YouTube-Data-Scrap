import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'truncate',
  standalone: true // Mark as standalone
})
export class TruncatePipe implements PipeTransform {

  transform(value: string, limit: number = 150, completeWords: boolean = false, ellipsis: string = '...') {
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
