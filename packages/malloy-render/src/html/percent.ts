/*
 * Copyright 2021 Google LLC
 *
 * This program is free software; you can redistribute it and/or
 * modify it under the terms of the GNU General Public License
 * version 2 as published by the Free Software Foundation.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
 * GNU General Public License for more details.
 */

import { DataValue } from "../data_table";
import { HtmlNumberRenderer } from "./number";

export class HtmlPercentRenderer extends HtmlNumberRenderer {
  getText(data: DataValue): string | null {
    const num = this.getNumber(data);

    return num === null
      ? num
      : (num * 100).toLocaleString("en", { maximumFractionDigits: 2 }) + "%";
  }
}
